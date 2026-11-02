# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_62`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_62/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 39 |
| Player Tracks | 39 |
| Ball Tracks | 0 |
| CSV events parsed | 25 |
| Action Segments inferred | 94 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [84–94], lower_priority='Action_ZoneBlock' annotated_start=90, effective_Action_ZoneBlock_start=95.
> - Action 'Action_None' range [84-260] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-280] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-297] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-273] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [112-197] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [202-204] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [210-263] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [265-278] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [282-289] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [84-299] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-299] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [84-94] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-275] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [84-149] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-299] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [84-275] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-236] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-256] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [90-98] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [110-134] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-192] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [196-299] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-271] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-86] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [90-106] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [114-115] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [120-128] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-142] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [90-94] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-167] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-189] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [196-299] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-134] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-135] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-275] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [156-162] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-179] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-297] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [196-197] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-218] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-255] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-266] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-271] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [269-273] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [279-280] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-296] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-282] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-291] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-294] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-277] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-284] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-290] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [292-296] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [295-299] for track '38' has 1 frames without a visible bounding box.
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
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.