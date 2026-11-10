# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_2`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_2/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 29 |
| Ball Tracks | 1 |
| CSV events parsed | 17 |
| Action Segments inferred | 83 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_None' range [84-199] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-186] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-193] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [85-104] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [85-113] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-190] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-203] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-203] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [84-269] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-178] for track '8' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [84-106] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [109-115] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [85-95] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [97-129] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [132-143] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [149-214] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-201] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [85-94] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-150] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-203] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-124] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-149] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-171] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-183] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-197] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-22] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-32] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-39] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-83] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' for track '14' starts at frame 84, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [84-112] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PullBall' range [120-123] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-176] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-195] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-124] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-128] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-265] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-147] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-161] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [165-213] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-233] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-237] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-199] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-203] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-213] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-167] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-269] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-187] for track '24' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [193-209] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-206] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-250] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [254-260] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [234-235] for track '29' has 1 frames without a visible bounding box.
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
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.