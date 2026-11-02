# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_203`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_203/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 22 |
| Player Tracks | 22 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 75 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Validation warning: Action 'Action_LeadBlock' for track '1' (TE2) duration 92 frames exceeds threshold 90 frames [start=121, end=212].
> - Validation warning: Action 'Action_ZoneBlock' for track '12' (C) duration 92 frames exceeds threshold 90 frames [start=121, end=212].
> - Validation warning: Action 'Action_ZoneBlock' for track '14' (RG) duration 92 frames exceeds threshold 90 frames [start=121, end=212].
> - Validation warning: Action 'Action_ZoneBlock' for track '19' (RT) duration 92 frames exceeds threshold 90 frames [start=121, end=212].
> - Validation warning: Action 'Action_ZoneBlock' for track '20' (LG) duration 92 frames exceeds threshold 90 frames [start=121, end=212].
> - Validation warning: Action 'Action_ZoneBlock' for track '21' (LT) duration 92 frames exceeds threshold 90 frames [start=121, end=212].
> - Action 'Action_None' range [108-269] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-269] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [138-207] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [209-234] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [239-264] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [266-268] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-254] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-267] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [108-151] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-214] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-219] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-243] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [121-212] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-269] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-269] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-129] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-159] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' for track '19' starts at frame 121, but the player has no visible bounding box on this frame.
> - Action 'Action_ZoneBlock' range [121-121] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [123-145] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [156-212] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-12] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-41] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-44] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-51] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' for track '20' starts at frame 121, but the player has no visible bounding box on this frame.
> - Action 'Action_ZoneBlock' range [121-121] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [124-126] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [128-129] for track '20' has 1 frames without a visible bounding box.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.