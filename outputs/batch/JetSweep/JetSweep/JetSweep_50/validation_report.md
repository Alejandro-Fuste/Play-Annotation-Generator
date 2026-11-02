# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_50`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_50/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 25 |
| Action Segments inferred | 91 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [48–63], lower_priority='Action_ZoneBlock' annotated_start=50, effective_Action_ZoneBlock_start=64.
> - Action 'Action_None' range [48-358] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [83-103] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '1' starts at frame 110, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [110-112] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [48-140] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-337] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [48-168] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-173] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-275] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-110] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-178] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [180-253] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-389] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-266] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [50-72] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [74-79] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [82-99] for track '8' has 4 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [101-108] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-112] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-120] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-217] for track '8' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [228-285] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [48-303] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-389] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [50-68] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '13' starts at frame 110, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [110-296] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [50-75] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [81-86] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [79-144] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [151-166] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [170-377] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [379-382] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [50-98] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-152] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-315] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [64-81] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [83-99] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-297] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [302-374] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [377-380] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [382-389] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [50-58] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [61-83] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-88] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-206] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [208-321] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-359] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-101] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-105] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-352] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-120] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-296] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [155-262] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-227] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-233] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-362] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [360-361] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [361-373] for track '29' has 1 frames without a visible bounding box.
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