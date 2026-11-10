# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_69`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_69/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 90 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [39-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-166] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-178] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [40-79] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [81-98] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [109-112] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-95] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-47] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-70] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [78-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-77] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-108] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-117] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-153] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-88] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [90-91] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-118] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-142] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [145-180] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [51-180] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [39-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [40-45] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-38] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' for track '17' starts at frame 40, but the player has no visible bounding box on this frame.
> - Action 'Action_ZoneBlock' range [40-40] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [46-96] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [102-104] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-107] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-78] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [80-81] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-84] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-180] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [105-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-38] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [40-47] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [57-104] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [105-120] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-138] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-38] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-123] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [129-133] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-46] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-92] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [97-134] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-139] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-111] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [135-178] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-180] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-180] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-180] for track '28' has 1 frames without a visible bounding box.
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