# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_16`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_16/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 27 |
| Action Segments inferred | 87 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [72–85], lower_priority='Action_ZoneBlock' annotated_start=78, effective_Action_ZoneBlock_start=86.
> - Action 'Action_ZoneBlock' range [78-95] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [98-140] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-165] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [78-140] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-212] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [78-90] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-105] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [78-92] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [96-100] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [103-140] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-206] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-230] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-178] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-239] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-102] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-227] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-239] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-69] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-213] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [218-223] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-75] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-116] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-125] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-144] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-163] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_Toss' range [92-160] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-66] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-92] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-100] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-94] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-20] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-196] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-27] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-33] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-4] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-16] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-71] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [72-82] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [100-101] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [77-95] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [98-198] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [205-206] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [208-217] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-112] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-214] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-239] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [119-126] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [147-176] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-189] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-228] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-140] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-142] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-174] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-239] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-223] for track '28' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.