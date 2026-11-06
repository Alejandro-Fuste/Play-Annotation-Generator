# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_36`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_36/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 73 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 74: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - Row 74: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_ZoneBlock' range [92-126] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-156] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-161] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-169] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-269] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [92-105] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [108-126] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-102] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-120] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-237] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-258] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-235] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-42] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [100-104] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-142] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-213] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-234] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-261] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [267-269] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-134] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [92-118] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-269] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-107] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-125] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-241] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-229] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-5] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-90] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-95] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-167] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-183] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-208] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-239] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-260] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-99] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-141] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-269] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-269] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-140] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-161] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-117] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-159] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-189] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-149] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-162] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-206] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-209] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-204] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-217] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-220] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-237] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-269] for track '24' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-269] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-217] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-237] for track '28' has 1 frames without a visible bounding box.
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