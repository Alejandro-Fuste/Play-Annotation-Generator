# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_282`
- **Input XML**: `outputs/batch/Power/Power/Power_282/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 22 |
| Player Tracks | 22 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 38 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Action 'Action_PreSnap' range [18-299] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-262] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-359] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [232-267] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-315] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [290-305] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [232-243] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [246-256] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-158] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-264] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [266-356] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [269-272] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [303-309] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [312-333] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [338-339] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [350-354] for track '17' has 1 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.