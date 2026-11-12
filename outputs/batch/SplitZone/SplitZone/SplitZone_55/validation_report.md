# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_55`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_55/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 88 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 569 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
> - Segment 'Action_BallCarry' for track '4' has invalid range: start=393, end=392. Clamping end to start.
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [369–380], lower_priority='Action_ZoneBlock' annotated_start=372, effective_Action_ZoneBlock_start=381.
> - Action 'Action_None' range [369-417] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [431-448] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [369-500] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [369-557] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [561-569] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [459-501] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-392] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [369-465] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [369-474] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [477-569] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [369-444] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [447-460] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [369-415] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [369-569] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [369-569] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [381-393] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '14' starts at frame 459, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [459-459] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [464-465] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [369-425] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [372-399] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [459-542] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [563-569] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [372-447] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [372-389] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [397-398] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [408-410] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [459-472] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [475-476] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [402-487] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [500-510] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [419-431] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [451-471] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [489-490] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [497-510] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [512-534] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [539-542] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [513-516] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [518-519] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [521-525] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [541-547] for track '29' has 2 frames without a visible bounding box.
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