# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_180`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_180/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 68 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 362: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - Row 362: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_None' range [36-139] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-78] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-55] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-65] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [37-67] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_Toss' range [59-63] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-82] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-50] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-107] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-112] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-136] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-83] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-28] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-82] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [37-79] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-97] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [107-126] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [130-155] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [37-55] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-27] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-81] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [37-52] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [58-61] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [72-73] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [37-117] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-148] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-20] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-24] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-147] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [24-63] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [64-110] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [42-86] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-80] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-87] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [82-94] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-108] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-152] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-250] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [119-220] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-141] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-156] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-156] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-269] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-181] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-233] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-267] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [258-261] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-267] for track '27' has 1 frames without a visible bounding box.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.