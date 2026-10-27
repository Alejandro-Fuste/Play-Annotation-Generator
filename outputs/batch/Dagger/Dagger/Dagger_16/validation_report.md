# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Dagger_16`
- **Input XML**: `outputs/batch/Dagger/Dagger/Dagger_16/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Dagger.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 92 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 509 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 509 as fallback play end.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [190–204], lower_priority='Action_PassBlock' annotated_start=193, effective_Action_PassBlock_start=205.
> - Action 'Action_None' range [190-424] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-503] for track '1' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [190-507] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [193-318] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [324-325] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [359-361] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [370-390] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [190-301] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [304-313] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-363] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [365-403] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [405-407] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-349] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-369] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-463] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [466-467] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [475-482] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [484-509] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-400] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [406-412] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [205-425] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-304] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-509] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-463] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [466-476] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [480-481] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [486-487] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [496-509] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-340] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [342-509] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [193-428] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [193-472] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-435] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [437-463] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [466-468] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [470-477] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [480-509] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [190-393] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [396-397] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [408-409] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [193-448] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-226] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-260] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-267] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-306] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [378-379] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-482] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-404] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-355] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [360-361] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [411-447] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [449-452] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [455-460] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [467-472] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [476-480] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [484-497] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [502-503] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [507-508] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [457-459] for track '29' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.