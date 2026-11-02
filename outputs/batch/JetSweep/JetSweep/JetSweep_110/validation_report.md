# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_110`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_110/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 75 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '4' (RT) duration 92 frames exceeds threshold 90 frames [start=76, end=167].
> - Validation warning: Action 'Action_ZoneBlock' for track '17' (RG) duration 92 frames exceeds threshold 90 frames [start=76, end=167].
> - Validation warning: Action 'Action_ZoneBlock' for track '18' (C) duration 92 frames exceeds threshold 90 frames [start=76, end=167].
> - Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [68–80], lower_priority='Action_ZoneBlock' annotated_start=76, effective_Action_ZoneBlock_start=81.
> - Validation warning: Action 'Action_ZoneBlock' for track '19' (LT) duration 92 frames exceeds threshold 90 frames [start=76, end=167].
> - Validation warning: Action 'Action_ZoneBlock' for track '21' (LG) duration 92 frames exceeds threshold 90 frames [start=76, end=167].
> - Action 'Action_None' range [68-239] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [68-205] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-211] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-221] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [76-145] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [148-152] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [103-222] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [68-116] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-173] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-222] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-188] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-211] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-232] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-195] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-202] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-215] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [222-227] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-232] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [76-113] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [81-95] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-239] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-137] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [147-150] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-154] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-155] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-202] for track '25' has 2 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.