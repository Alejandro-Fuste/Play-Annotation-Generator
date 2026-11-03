# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Slants0to10_83`
- **Input XML**: `outputs/batch/Slants0to10/Slants0to10/Slants0to10_83/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Slants0to10.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 40 |
| Player Tracks | 40 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 110 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 84: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - Row 84: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-168] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-181] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-190] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-224] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-238] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-251] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [256-261] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-193] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-208] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-225] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-269] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-14] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-95] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-157] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-136] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-157] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-179] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_RunSlantRoute' range [4-66] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [81-102] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [106-107] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-219] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-228] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-237] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-269] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-64] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-70] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-91] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-14] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-61] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-51] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-61] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [2-38] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [40-61] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [67-75] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-113] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-116] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-123] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [2-27] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [29-48] for track '15' has 6 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-118] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-135] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-178] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-269] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-48] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-140] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-147] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-165] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [2-16] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [18-32] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [34-63] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [65-66] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [68-82] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [2-15] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [18-63] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [68-78] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [83-84] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-221] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [2-7] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [22-28] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-35] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-48] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-98] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-60] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-85] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-90] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-95] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-95] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-105] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-95] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-165] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-131] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-176] for track '29' has 6 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-193] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-201] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-138] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-141] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-179] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-184] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-163] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-171] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-176] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-181] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-196] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-209] for track '33' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-230] for track '33' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-237] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-244] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-167] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-165] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-211] for track '36' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-176] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-216] for track '38' has 1 frames without a visible bounding box.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
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
> - Play definition: no definition found for 'Play_Pass_Slants0to10'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.