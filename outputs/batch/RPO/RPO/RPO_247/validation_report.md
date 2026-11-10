# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_247`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_247/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 38 |
| Player Tracks | 38 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 142 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Segment 'Action_RunBlock' for track '21' has invalid range: start=47, end=16. Clamping end to start.
> - Action 'Action_None' range [46-106] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-299] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-74] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-123] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-126] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-299] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-123] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-299] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-123] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [131-278] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-299] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-284] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [47-108] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-123] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [46-198] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-197] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-69] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-75] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-122] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [128-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-167] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-172] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-175] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-103] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-123] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-126] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-263] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [56-123] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [128-134] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-105] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [107-123] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-126] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-299] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-75] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [77-80] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [82-123] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [125-126] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-45] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [47-52] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [60-65] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [67-99] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [104-105] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-118] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-121] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-176] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-182] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-61] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-192] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-234] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-242] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-263] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-278] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-281] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '18' starts at frame 46, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [46-46] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [51-52] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-140] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-14] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-45] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [47-60] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [83-100] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [102-107] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [119-123] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-126] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-299] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-13] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-38] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '20' starts at frame 46, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [46-57] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PullBall' range [75-82] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-8] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-16] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-20] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-26] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-50] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-57] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-95] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [103-104] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-116] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-109] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-122] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-139] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-144] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-278] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [280-299] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-161] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-182] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-299] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-168] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-176] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-180] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-187] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [190-193] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-175] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-191] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-208] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [211-252] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-194] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-218] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-239] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-245] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-249] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-255] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-278] for track '36' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [298-299] for track '37' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.