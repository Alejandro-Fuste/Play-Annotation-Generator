# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_184`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_184/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 107 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '1' (LG) duration 94 frames exceeds threshold 90 frames [start=26, end=119].
> - Overlapping action conflict at frame 26 for track '3': 'Action_ZoneBlock' vs 'Action_LeadBlock'. Overriding with 'Action_LeadBlock'.
> - Validation warning: Action 'Action_LeadBlock' for track '3' (RT) duration 94 frames exceeds threshold 90 frames [start=26, end=119].
> - Validation warning: Action 'Action_ZoneBlock' for track '7' (RG) duration 94 frames exceeds threshold 90 frames [start=26, end=119].
> - Action 'Action_None' range [25-67] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-100] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-106] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-122] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [26-49] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [57-67] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [26-43] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [45-61] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [63-76] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [26-44] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [51-55] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [57-105] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-132] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-48] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-114] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-73] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-134] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [26-73] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [76-91] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-125] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-29] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-77] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [80-81] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-85] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-92] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-95] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-137] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-37] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-53] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-81] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [83-146] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [150-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-115] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-146] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-168] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [177-178] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-48] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-110] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-117] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-183] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [52-55] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [59-142] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [144-168] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-41] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-57] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-74] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-42] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-160] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-61] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-90] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-112] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [114-152] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-48] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-70] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [73-136] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-92] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-103] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-164] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-194] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-114] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [74-75] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-173] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [178-182] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-110] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [81-168] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-114] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-144] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-157] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-192] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-210] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [128-180] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-171] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-149] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-174] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [178-180] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-210] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-164] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-210] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-210] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-210] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-196] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-210] for track '35' has 1 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.