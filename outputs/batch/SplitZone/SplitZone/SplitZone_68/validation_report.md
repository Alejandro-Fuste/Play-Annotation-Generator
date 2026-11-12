# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_68`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_68/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 29 |
| Ball Tracks | 1 |
| CSV events parsed | 21 |
| Action Segments inferred | 65 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 479 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
> - Resolved action overlap for track '4' (C): higher_priority='Action_BallSnap' [285–299], lower_priority='Action_ZoneBlock' annotated_start=288, effective_Action_ZoneBlock_start=300.
> - Action 'Action_SplitBlock' range [288-349] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [370-391] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [288-369] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [370-421] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [370-422] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-377] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [300-344] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [348-355] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' for track '5' starts at frame 320, but the player has no visible bounding box on this frame.
> - Action 'Action_BallCarry' range [320-476] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [370-404] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [409-431] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-459] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [285-432] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [288-369] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [370-419] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-335] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [338-355] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [357-433] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [304-319] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-400] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-50] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-348] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [360-364] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [368-380] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [382-392] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [395-424] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-70] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-268] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [331-470] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [340-375] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-358] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [362-415] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [383-407] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [385-467] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [386-455] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [387-392] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [405-406] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [459-464] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [474-475] for track '29' has 1 frames without a visible bounding box.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
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