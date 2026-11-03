# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutRoutes_27`
- **Input XML**: `outputs/batch/OutRoutes/OutRoutes/OutRoutes_27/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutRoutes.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 39 |
| Player Tracks | 39 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 102 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Segment 'Action_BallCarry' for track '4' has invalid range: start=99, end=78. Clamping end to start.
> - Segment 'Action_PassBlock' for track '21' has invalid range: start=14, end=7. Clamping end to start.
> - Action 'Action_PreSnap' range [0-160] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-43] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-18] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-27] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-50] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-54] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-61] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-70] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-77] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-83] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-92] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-241] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-59] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-71] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-78] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-113] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-200] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-61] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-67] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-78] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-11] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [47-48] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [68-69] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-73] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-80] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-87] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-30] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_SecureCatch' range [90-153] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_SecureCatch' range [160-171] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_SecureCatch' range [181-200] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-167] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-269] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-16] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-41] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-18] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-31] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-43] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-174] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-109] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-121] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-127] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-132] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-137] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-147] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-260] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-11] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-14] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-10] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [33-35] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-10] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' for track '19' starts at frame 14, but the player has no visible bounding box on this frame.
> - Action 'Action_PassBlock' range [14-16] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [31-41] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [75-83] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [87-245] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-13] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' for track '20' starts at frame 14, but the player has no visible bounding box on this frame.
> - Action 'Action_PassBlock' range [14-14] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [98-102] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-244] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [246-253] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-160] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-108] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-155] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-212] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-114] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-121] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-211] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-202] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-107] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-123] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-239] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-161] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-122] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-206] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-122] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-147] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-209] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-203] for track '33' has 1 frames without a visible bounding box.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.