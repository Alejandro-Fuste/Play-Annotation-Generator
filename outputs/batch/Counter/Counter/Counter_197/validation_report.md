# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_197`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_197/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 75 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_None' range [153-198] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-277] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-244] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-223] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-229] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-299] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-208] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-224] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-232] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-232] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-299] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-222] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [224-228] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [153-299] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-239] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-176] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [157-170] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [190-196] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [201-204] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-239] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-267] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [157-184] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [153-200] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [153-299] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-74] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [157-176] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [189-237] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-52] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-228] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-271] for track '27' has 1 frames without a visible bounding box.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.