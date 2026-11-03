# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutRoutes_77`
- **Input XML**: `outputs/batch/OutRoutes/OutRoutes/OutRoutes_77/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutRoutes.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 97 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 84: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - Row 84: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - Row 84: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-210] for track '0' has 4 frames without a visible bounding box.
> - Action 'Action_RunOutRoute' range [30-210] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [123-200] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-95] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-207] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-181] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-210] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-66] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-91] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-111] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-210] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-83] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-110] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-166] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-162] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-109] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-210] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-161] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-210] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-129] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-153] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-210] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-115] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-135] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-81] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-112] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-153] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-168] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-182] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [25-34] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [70-72] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-192] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-200] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [25-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-44] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-66] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-74] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-81] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-210] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [25-35] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [37-48] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [50-51] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [53-54] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [59-62] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [25-54] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [56-57] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [65-67] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [69-99] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-61] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-81] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-96] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-99] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-108] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-115] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-100] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-110] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-135] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-120] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-164] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-205] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-122] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-180] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-185] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-202] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-208] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-149] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-164] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-168] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-176] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-180] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-191] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-195] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-209] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-181] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-189] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-197] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-197] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-201] for track '33' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.