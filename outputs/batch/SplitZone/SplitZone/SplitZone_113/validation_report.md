# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_113`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_113/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 152 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 839 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 839 as fallback play end.
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [702–715], lower_priority='Action_ZoneBlock' annotated_start=705, effective_Action_ZoneBlock_start=716.
> - Segment 'Action_ZoneBlock' for track '22' has invalid range: start=705, end=340. Clamping end to start.
> - Action 'Action_None' range [702-837] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [702-746] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [749-762] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [794-810] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [814-815] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [819-839] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [703-763] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [768-770] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [702-817] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [819-839] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [702-768] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [773-835] for track '6' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [702-763] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [768-771] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [789-809] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [813-839] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [702-839] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [702-831] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [702-805] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-34] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-78] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-332] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [338-340] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [342-348] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [351-358] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [361-704] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [705-728] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [730-763] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [800-807] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [810-811] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [813-839] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-52] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-55] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-704] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [705-763] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-48] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-312] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [315-324] for track '13' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [374-375] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [386-387] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [389-390] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [397-398] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [401-481] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [483-701] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [702-758] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [761-762] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [822-825] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [827-836] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-59] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-63] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-328] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [331-332] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [335-507] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [509-530] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [539-540] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [545-548] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [550-701] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [702-732] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [735-762] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-21] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-52] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-55] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-59] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-63] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-332] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [372-376] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [716-717] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [726-730] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [723-728] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-40] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-44] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-48] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-52] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-55] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-77] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-363] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [702-741] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [746-751] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-12] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-17] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-701] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [702-763] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-324] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [339-701] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [723-762] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-33] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-52] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-55] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-85] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-92] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [705-726] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [728-735] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [814-815] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [819-820] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [823-839] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-7] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-12] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-17] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-33] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-77] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-167] for track '22' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-174] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-332] for track '22' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [339-340] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-83] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-253] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [562-573] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [702-763] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [741-742] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [762-766] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [827-829] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [835-836] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [773-774] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [782-820] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [823-825] for track '32' has 1 frames without a visible bounding box.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.