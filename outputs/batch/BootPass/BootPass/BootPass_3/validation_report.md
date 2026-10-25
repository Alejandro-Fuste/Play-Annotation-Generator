# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `BootPass_3`
- **Input XML**: `outputs/batch/BootPass/BootPass/BootPass_3/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 41 |
| Player Tracks | 41 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 147 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 8: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - Row 8: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [12–27], lower_priority='Action_RunBlock' annotated_start=17, effective_Action_RunBlock_start=28.
> - Action 'Action_None' range [12-81] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-110] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-107] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-182] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-254] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-305] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [310-312] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-318] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-327] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [330-331] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-335] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [340-343] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-108] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-60] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-120] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [132-133] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-147] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-159] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [167-168] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-195] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-206] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-297] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-89] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [92-177] for track '6' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-176] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-196] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [198-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-299] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [302-334] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [12-108] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-131] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [145-147] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-117] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-108] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ThrowPass' range [135-141] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-117] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-155] for track '12' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [159-168] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [17-102] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-32] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-48] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-28] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-31] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-66] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-107] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-113] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-91] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-110] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-181] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-292] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [311-319] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-322] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-327] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-359] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-202] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [217-294] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [298-299] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-304] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-313] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-331] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-11] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-194] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [12-19] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [28-65] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [74-106] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [17-131] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [17-40] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [42-119] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [54-55] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-109] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-119] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [65-73] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-78] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-102] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-121] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [145-147] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-167] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-110] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-151] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [153-159] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-117] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-150] for track '28' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [152-184] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-190] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [145-155] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [149-153] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-161] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-210] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [213-215] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-220] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-281] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-204] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-214] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-303] for track '33' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [311-331] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-359] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-359] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-264] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-341] for track '35' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [343-348] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [358-359] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-260] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-265] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-270] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-296] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [302-309] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-292] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-277] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-281] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-298] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-327] for track '40' has 1 frames without a visible bounding box.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.