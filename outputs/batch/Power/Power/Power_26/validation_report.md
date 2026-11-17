# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_26`
- **Input XML**: `outputs/batch/Power/Power/Power_26/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 48 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 54: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_PreSnap' range [25-214] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [144-167] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [176-182] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-153] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-192] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-296] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-172] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-182] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-251] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-299] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-119] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-165] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-221] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-256] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-299] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [144-161] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [163-174] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [208-299] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-141] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-218] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-233] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-246] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-253] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-256] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-197] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-147] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-205] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-208] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-299] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-261] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [267-277] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-298] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-220] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-246] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-299] for track '22' has 1 frames without a visible bounding box.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.