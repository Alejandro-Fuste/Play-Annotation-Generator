# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_278`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_278/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 88 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '7' (C): higher_priority='Action_BallSnap' [10–27], lower_priority='Action_ZoneBlock' annotated_start=13, effective_Action_ZoneBlock_start=28.
> - Action 'Action_None' range [10-75] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-63] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-148] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-152] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-171] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-88] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-123] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [13-82] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-94] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-114] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-43] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-46] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-51] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-64] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_Keep' range [40-55] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_Keep' range [57-58] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [67-76] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [88-91] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [93-108] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [110-115] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [118-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [28-53] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [79-82] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-91] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-96] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-102] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-56] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-107] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-22] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [13-36] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [55-56] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [63-66] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [10-81] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-110] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [13-22] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-157] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [10-32] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-79] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [28-38] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-41] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-52] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [60-64] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-96] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-103] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-137] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-117] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-75] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-180] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [75-111] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [83-85] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-89] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-180] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [91-103] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-96] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-114] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [137-180] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-127] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-121] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-159] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-180] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-180] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-180] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-180] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-156] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-158] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-180] for track '32' has 2 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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