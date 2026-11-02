# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_111`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_111/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 80 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '3' (LT) duration 100 frames exceeds threshold 90 frames [start=78, end=177].
> - Validation warning: Action 'Action_ZoneBlock' for track '6' (LG) duration 100 frames exceeds threshold 90 frames [start=78, end=177].
> - Validation warning: Action 'Action_ZoneBlock' for track '7' (RT) duration 100 frames exceeds threshold 90 frames [start=78, end=177].
> - Validation warning: Action 'Action_ZoneBlock' for track '10' (RG) duration 100 frames exceeds threshold 90 frames [start=78, end=177].
> - Validation warning: Action 'Action_LeadBlock' for track '11' (RB) duration 100 frames exceeds threshold 90 frames [start=78, end=177].
> - Validation warning: Action 'Action_ZoneBlock' for track '15' (C) duration 100 frames exceeds threshold 90 frames [start=78, end=177].
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [76–90], lower_priority='Action_ZoneBlock' annotated_start=78, effective_Action_ZoneBlock_start=91.
> - Action 'Action_None' range [76-97] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-239] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [76-134] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-163] for track '2' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [165-210] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [213-220] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [78-162] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [166-170] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-146] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [153-154] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-231] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [78-109] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [111-136] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [144-160] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [167-177] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' for track '6' starts at frame 178, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [178-184] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [192-239] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-239] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-108] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-165] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-182] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [201-209] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-214] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-237] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-173] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-190] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [78-123] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-184] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [78-169] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-131] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-107] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [115-116] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-175] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [76-95] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [111-201] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [217-218] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [220-221] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-137] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-181] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [134-139] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-145] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-176] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-162] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-199] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [201-214] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-238] for track '26' has 1 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.