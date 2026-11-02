# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_97`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_97/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 39 |
| Player Tracks | 39 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 87 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [46–61], lower_priority='Action_ZoneBlock' annotated_start=50, effective_Action_ZoneBlock_start=62.
> - Action 'Action_None' range [46-102] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-130] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-231] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [235-243] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-128] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [46-96] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-115] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-119] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-123] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-210] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [213-243] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [250-302] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-187] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-121] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-110] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-117] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-108] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-110] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-120] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-119] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-113] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-129] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-110] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [75-102] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [117-159] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [95-102] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-114] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-218] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-143] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-155] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-220] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [167-294] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-185] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-248] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-261] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-279] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-292] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [182-184] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-329] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-223] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-301] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-329] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-288] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-321] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-295] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-311] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [258-292] for track '32' has 2 frames without a visible bounding box.
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
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.