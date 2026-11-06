# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_88`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_88/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 27 |
| Ball Tracks | 1 |
| CSV events parsed | 15 |
| Action Segments inferred | 57 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 178: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_None' range [86-242] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [35-45] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-251] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [41-61] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-119] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-179] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-329] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-100] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-179] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [35-46] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-302] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-308] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-260] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-153] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-107] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-156] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-161] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-260] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-264] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-45] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-203] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-116] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-322] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-85] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-316] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-137] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-149] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-155] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-295] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [299-300] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-179] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-294] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-149] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-169] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-174] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-211] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-221] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-233] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-307] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-216] for track '27' has 1 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.