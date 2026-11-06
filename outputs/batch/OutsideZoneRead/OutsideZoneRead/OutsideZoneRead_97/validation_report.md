# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_97`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_97/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 119 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_None' range [1-211] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-269] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-36] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-256] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [261-269] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-93] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-230] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [232-235] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-269] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-134] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-129] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-136] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-156] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-128] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_Keep' for track '10' starts at frame 35, but the player has no visible bounding box on this frame.
> - Action 'Action_Keep' range [35-45] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [4-11] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [15-64] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-97] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-81] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-86] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-93] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-93] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [95-101] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-115] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-269] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-109] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-121] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-124] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-128] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-142] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-216] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [4-56] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-121] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [143-154] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [4-11] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [13-29] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [71-128] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [132-136] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [4-11] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [38-47] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [56-57] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-19] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-75] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [5-18] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [20-36] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [39-67] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-72] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-88] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [90-96] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [103-108] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-213] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-115] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-118] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-136] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [139-150] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-172] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [187-188] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-192] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-136] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-172] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-180] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-185] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [187-197] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [199-202] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-153] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-192] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [164-166] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-192] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-269] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-218] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-247] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-269] for track '34' has 3 frames without a visible bounding box.
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
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.