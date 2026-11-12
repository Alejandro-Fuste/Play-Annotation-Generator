# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_284`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_284/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 77 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 749 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 570: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 749 as fallback play end.
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [516–528], lower_priority='Action_ZoneBlock' annotated_start=527, effective_Action_ZoneBlock_start=529.
> - Action 'Action_None' range [516-639] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [516-541] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [516-742] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [516-574] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [516-571] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [549-749] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [516-545] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [558-634] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [641-645] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [648-658] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [686-725] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [727-728] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [527-598] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [516-727] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [516-563] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [570-749] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [516-634] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [639-686] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [516-656] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [660-670] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [678-683] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [558-560] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [567-569] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [578-582] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [623-629] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [674-676] for track '26' has 1 frames without a visible bounding box.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
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