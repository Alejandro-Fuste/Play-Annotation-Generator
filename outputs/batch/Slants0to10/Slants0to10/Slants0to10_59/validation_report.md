# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Slants0to10_59`
- **Input XML**: `outputs/batch/Slants0to10/Slants0to10/Slants0to10_59/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Slants0to10.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 41 |
| Player Tracks | 41 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 114 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_BallCarry' range [93-182] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [193-194] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [196-201] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [204-207] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-106] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-115] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-182] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-204] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-79] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-25] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-31] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-125] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-173] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-192] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [7-162] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [164-165] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [177-178] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [180-182] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [190-239] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-136] for track '8' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-149] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-160] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-161] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-164] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-219] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-62] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-135] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-158] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-165] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-239] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [7-44] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-195] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-198] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-239] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-195] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [7-150] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [196-202] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-38] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-157] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-165] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-175] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [7-14] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [16-73] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [78-150] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [152-154] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [7-66] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [72-85] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-8] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-15] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-23] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-36] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-45] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-95] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-100] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-111] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-120] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-145] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-160] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-165] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-168] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-201] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-239] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-117] for track '24' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-120] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-93] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-99] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-106] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-120] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-138] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-107] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-160] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-127] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-153] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-179] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-232] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-177] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-184] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-217] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-194] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-239] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-202] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-220] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-239] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-202] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-211] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-233] for track '39' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-226] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-234] for track '40' has 2 frames without a visible bounding box.
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
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Play definition: no definition found for 'Play_Pass_Slants0to10'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.