# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_61`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_61/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 163 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_ZoneBlock' for track '18' has invalid range: start=44, end=35. Clamping end to start.
> - Segment 'Action_ZoneBlock' for track '20' has invalid range: start=44, end=35. Clamping end to start.
> - Action 'Action_None' range [43-204] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [43-74] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [77-210] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [43-73] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-82] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-92] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [95-205] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [207-210] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [106-129] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-167] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [169-172] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-199] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [201-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-38] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [54-65] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-82] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [84-157] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-194] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [196-198] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-203] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-182] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-185] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-196] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-38] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-47] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-70] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [77-82] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-100] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-201] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-36] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-143] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [149-210] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-38] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [55-57] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-62] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-70] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-82] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-85] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-92] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [94-129] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-156] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-194] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [201-203] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-208] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-58] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-38] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [45-47] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [55-61] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [67-70] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [78-82] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [85-105] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [106-129] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-142] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-155] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-188] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [196-210] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-35] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-38] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-35] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-42] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [44-45] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [56-60] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [64-65] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [67-70] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [77-82] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-159] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-35] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-38] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [45-47] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [53-61] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [70-105] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [106-136] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-151] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-178] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [184-186] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-195] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-200] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-207] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-210] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [56-71] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [77-82] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-129] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-141] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-151] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-157] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [165-190] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [60-70] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [60-76] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [78-82] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-107] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-118] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-123] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-129] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-132] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-168] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-172] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-191] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-199] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-111] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-87] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-91] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-94] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-99] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-114] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [116-117] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-124] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [126-127] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-135] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-148] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-155] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-163] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-102] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-115] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-151] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-156] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-174] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [176-190] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-194] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-198] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-202] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-209] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-121] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-130] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [132-137] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-142] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-146] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-162] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [170-210] for track '30' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [123-210] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-150] for track '32' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [176-177] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-195] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-210] for track '33' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [198-209] for track '34' has 3 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.