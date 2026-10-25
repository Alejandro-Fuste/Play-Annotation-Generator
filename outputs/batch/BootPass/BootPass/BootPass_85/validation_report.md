# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `BootPass_85`
- **Input XML**: `outputs/batch/BootPass/BootPass/BootPass_85/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 98 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [106–121], lower_priority='Action_RunBlock' annotated_start=114, effective_Action_RunBlock_start=122.
> - Action 'Action_None' range [106-232] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [220-257] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [259-359] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [106-359] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-306] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [326-350] for track '3' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [353-356] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-231] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-131] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-215] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-286] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [106-149] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-230] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-291] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-297] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-314] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [316-359] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [114-139] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [143-326] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [122-127] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [151-156] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [206-333] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-124] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-359] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-245] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-249] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-267] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-281] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-284] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-291] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-298] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-324] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [327-341] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [347-356] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-359] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [114-132] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [142-152] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [156-157] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [164-270] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [272-286] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [290-296] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [300-359] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [106-137] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-268] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-273] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-308] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-184] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [106-135] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [114-130] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [133-135] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [142-143] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [155-355] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [135-231] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [233-334] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-256] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-263] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-269] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-342] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-218] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-242] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-359] for track '26' has 1 frames without a visible bounding box.
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