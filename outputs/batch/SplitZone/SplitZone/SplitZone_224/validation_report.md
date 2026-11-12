# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_224`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_224/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 35 |
| Ball Tracks | 2 |
| CSV events parsed | 21 |
| Action Segments inferred | 89 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 449 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
> - Resolved action overlap for track '6' (C): higher_priority='Action_BallSnap' [301–305], lower_priority='Action_ZoneBlock' annotated_start=304, effective_Action_ZoneBlock_start=306.
> - Action 'Action_None' range [301-332] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-99] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-352] for track '2' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [355-356] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [358-367] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [371-378] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-194] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-363] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [367-368] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-134] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-449] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-362] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [368-394] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [397-399] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-250] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-300] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [301-305] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [338-429] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [431-432] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-64] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [338-427] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-449] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-27] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [391-416] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-43] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-48] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-51] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-69] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [304-347] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-110] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [304-359] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-349] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [351-388] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-350] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-150] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-300] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-400] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [301-315] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-342] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-444] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [352-363] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [362-366] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [369-449] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [378-388] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [390-405] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [385-439] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [409-410] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [421-423] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [437-439] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [433-435] for track '35' has 1 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.