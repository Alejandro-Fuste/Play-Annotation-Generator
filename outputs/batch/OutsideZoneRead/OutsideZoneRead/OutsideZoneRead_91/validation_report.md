# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_91`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_91/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 43 |
| Player Tracks | 42 |
| Ball Tracks | 1 |
| CSV events parsed | 17 |
| Action Segments inferred | 83 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Action 'Action_PreSnap' range [0-259] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-249] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [77-178] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-231] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-123] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-289] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-102] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-106] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-128] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-91] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ReadEdgeDefender' range [68-85] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_Keep' range [91-168] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [77-124] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-187] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-221] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-241] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [59-75] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-87] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-121] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-78] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-86] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-118] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-67] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [68-86] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [88-94] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-112] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-52] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [77-94] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-109] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-130] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-8] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-118] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-126] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-359] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-123] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-250] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-216] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-278] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-265] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-272] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-257] for track '24' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-190] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-237] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-193] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-203] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-253] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-263] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-227] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-230] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-359] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-204] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-349] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-298] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [301-304] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-230] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-248] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-254] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [330-337] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [353-354] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [346-348] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [350-354] for track '41' has 1 frames without a visible bounding box.
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
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.