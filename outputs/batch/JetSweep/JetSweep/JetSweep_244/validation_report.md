# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_244`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_244/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 71 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [43–56], lower_priority='Action_ZoneBlock' annotated_start=45, effective_Action_ZoneBlock_start=57.
> - Action 'Action_None' range [43-99] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-97] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [99-100] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-105] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-56] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-64] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [43-93] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-102] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-77] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-239] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [45-80] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-99] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [30-66] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [101-102] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [45-98] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '10' starts at frame 99, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [99-99] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-104] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [99-103] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [105-108] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-40] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [47-99] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-239] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-53] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-74] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [79-86] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [90-99] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-104] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-94] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-106] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '16' starts at frame 99, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [99-99] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-100] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-105] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-84] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-87] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-128] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-157] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [160-161] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-177] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [183-216] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-174] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-219] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [233-234] for track '24' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.