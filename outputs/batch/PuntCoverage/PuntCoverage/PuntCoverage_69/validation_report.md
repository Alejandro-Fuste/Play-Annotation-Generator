# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntCoverage_69`
- **Input XML**: `outputs/batch/PuntCoverage/PuntCoverage/PuntCoverage_69/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntCoverage.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 52 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_PreSnap' range [0-236] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-255] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-222] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-111] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-152] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-92] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-18] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-245] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-248] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-258] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-28] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-13] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_Tackle' range [216-223] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-222] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-230] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-116] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-139] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-222] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-230] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-230] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-131] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-164] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-169] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-194] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-248] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-264] for track '26' has 1 frames without a visible bounding box.
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
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.