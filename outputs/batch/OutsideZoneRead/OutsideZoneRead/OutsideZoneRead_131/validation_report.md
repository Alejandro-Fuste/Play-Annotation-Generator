# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_131`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_131/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 149 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [19–32], lower_priority='Action_ZoneBlock' annotated_start=22, effective_Action_ZoneBlock_start=33.
> - Action 'Action_None' range [19-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-111] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-117] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [121-122] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-183] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-206] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-74] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [76-94] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-97] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-105] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-210] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [19-208] for track '4' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [19-73] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-93] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [96-97] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-105] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-210] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [19-57] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-61] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-73] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-183] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [188-191] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-200] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [19-183] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-191] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-201] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-73] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-97] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [101-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-191] for track '10' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [19-57] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-74] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-94] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-97] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-105] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-210] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [19-57] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-61] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-73] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-93] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-97] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-105] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-210] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [22-57] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [60-61] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [64-66] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-89] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-210] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_Keep' range [47-64] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [65-163] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [33-34] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-35] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-57] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-61] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-73] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [76-84] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [86-94] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-97] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-116] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [22-57] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [59-62] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [64-74] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-94] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-97] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [22-57] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [60-61] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [66-69] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [77-79] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [83-84] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-94] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-97] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-105] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-210] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [19-57] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-61] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-73] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [76-82] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-94] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-97] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-105] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-202] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [205-206] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [22-35] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [37-51] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-69] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-73] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-84] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [92-93] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-97] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-183] for track '23' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [187-198] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-206] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-101] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [109-210] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [113-191] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-200] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [205-209] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-131] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-146] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-151] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-162] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-201] for track '27' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [203-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-122] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-157] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-160] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-176] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [182-183] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-191] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-196] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-202] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-208] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-198] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-198] for track '35' has 1 frames without a visible bounding box.
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
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.