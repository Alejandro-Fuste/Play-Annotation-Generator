# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_112`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_112/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 45 |
| Player Tracks | 45 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 141 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Validation warning: Action 'Action_PullBlock' for track '5' (RG) duration 102 frames exceeds threshold 90 frames [start=30, end=131].
> - Validation warning: Action 'Action_DownBlock' for track '7' (LG) duration 102 frames exceeds threshold 90 frames [start=30, end=131].
> - Validation warning: Action 'Action_DownBlock' for track '8' (LT) duration 102 frames exceeds threshold 90 frames [start=30, end=131].
> - Action 'Action_None' range [27-61] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-90] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [92-93] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-97] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-100] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-70] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-269] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [27-98] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [101-124] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [127-216] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-57] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-119] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-137] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-143] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-160] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-169] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [53-103] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [125-247] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [30-62] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [70-93] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [103-131] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-127] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [30-49] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [51-92] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [94-124] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-176] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [30-62] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [64-71] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [73-91] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [93-111] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [132-136] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-49] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-82] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-94] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-119] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [30-59] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [64-75] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [82-103] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [108-119] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [124-131] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-47] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [49-76] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-120] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-26] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [27-28] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-56] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-65] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-78] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-154] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-171] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-16] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '14' starts at frame 27, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [27-27] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-41] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-45] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-111] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-155] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-166] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-179] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [33-41] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [44-45] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-71] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [86-89] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-102] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-70] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-85] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-143] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-149] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-159] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-111] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-196] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-226] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [239-242] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-269] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-114] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [116-117] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-198] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [135-159] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-168] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-177] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-185] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-217] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-144] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-202] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-235] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-269] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [142-162] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-173] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-147] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-178] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-185] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-236] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [238-267] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-185] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-190] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-198] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [200-249] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-191] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-240] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-252] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-239] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-198] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-198] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-217] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-221] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-225] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-269] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-224] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-233] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-225] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-240] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-269] for track '43' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.
> - Player track '44' has undefined position. Will map to Position_Unknown.
> - Player track '44' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.