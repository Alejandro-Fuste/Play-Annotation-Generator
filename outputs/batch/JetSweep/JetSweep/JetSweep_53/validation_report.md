# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_53`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_53/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 71 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [116–129], lower_priority='Action_ZoneBlock' annotated_start=120, effective_Action_ZoneBlock_start=130.
> - Action 'Action_None' range [116-142] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-186] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-160] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [120-166] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-299] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [120-157] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-156] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-184] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [120-173] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-187] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-145] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-131] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-221] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [130-166] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [168-169] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-156] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-193] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-178] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-184] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-107] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-115] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [116-119] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-138] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-190] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-122] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [117-290] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-179] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-133] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [171-183] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [171-198] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_SealBlock' range [186-228] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [184-234] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-253] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-276] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [187-292] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [296-298] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-261] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-281] for track '32' has 1 frames without a visible bounding box.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.