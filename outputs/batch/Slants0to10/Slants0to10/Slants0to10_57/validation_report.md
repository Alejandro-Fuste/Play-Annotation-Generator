# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Slants0to10_57`
- **Input XML**: `outputs/batch/Slants0to10/Slants0to10/Slants0to10_57/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Slants0to10.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 142 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 57: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - Row 58: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - Row 58: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_PassBlock' for track '13' has invalid range: start=4, end=1. Clamping end to start.
> - Action 'Action_None' range [1-111] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-128] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-239] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-44] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-66] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-75] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-84] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [99-100] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-104] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-118] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-126] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [183-196] for track '4' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [199-209] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [212-221] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [226-239] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-143] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-151] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-206] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-91] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-103] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [117-118] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-177] for track '7' has 10 frames without a visible bounding box.
> - Action 'Action_None' range [180-186] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-197] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-239] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-25] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-38] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-44] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-95] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-6] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-23] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-29] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-44] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-84] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [91-92] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-101] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [107-110] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-222] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [93-239] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-14] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' for track '12' starts at frame 4, but the player has no visible bounding box on this frame.
> - Action 'Action_PassBlock' range [4-4] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [10-15] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [18-20] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [23-25] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [41-73] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [77-90] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-29] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-35] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [41-84] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [29-30] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-33] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-44] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-57] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-64] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-70] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-84] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [87-134] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [149-239] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [31-122] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-58] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-65] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-96] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-100] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-44] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-49] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-62] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-44] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-58] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-70] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-43] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-121] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-136] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-145] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-178] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [182-207] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-239] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-56] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-70] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [72-147] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [149-151] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-239] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [56-84] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-120] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-126] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-70] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-81] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-125] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-221] for track '26' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [149-155] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [165-166] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-153] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-156] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-159] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-167] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-161] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-196] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [198-239] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [163-169] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-187] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-196] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [199-209] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [211-239] for track '32' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [168-239] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [180-196] for track '34' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [198-239] for track '34' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [185-197] for track '35' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [199-202] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-209] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-221] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [224-230] for track '35' has 2 frames without a visible bounding box.
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
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Play definition: no definition found for 'Play_Pass_Slants0to10'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.