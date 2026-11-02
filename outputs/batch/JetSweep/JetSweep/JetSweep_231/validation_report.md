# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_231`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_231/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 96 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [47–61], lower_priority='Action_ZoneBlock' annotated_start=48, effective_Action_ZoneBlock_start=62.
> - Action 'Action_None' range [47-150] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [48-89] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [134-239] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-188] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-206] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [210-211] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-239] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [47-89] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [91-175] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-165] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [168-185] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [47-118] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-145] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [48-100] for track '8' has 5 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [1-70] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [72-109] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [47-82] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-89] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-105] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-84] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-103] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-125] for track '12' has 4 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [62-69] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-141] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-146] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-165] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [168-239] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [70-207] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [209-228] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [230-239] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-239] for track '16' has 7 frames without a visible bounding box.
> - Action 'Action_None' range [47-239] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [48-84] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [48-105] for track '21' has 5 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [108-114] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-63] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-114] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [129-162] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-168] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-178] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [180-183] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [185-205] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-239] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-145] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-201] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [190-193] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [196-202] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-208] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-228] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-239] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-239] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-226] for track '32' has 1 frames without a visible bounding box.
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