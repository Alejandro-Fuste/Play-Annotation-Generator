# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_170`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_170/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 53 |
| Player Tracks | 53 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 152 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Track ID '22' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '17' (RT) duration 100 frames exceeds threshold 90 frames [start=3, end=102].
> - Validation warning: Action 'Action_PullBlock' for track '19' (C) duration 100 frames exceeds threshold 90 frames [start=3, end=102].
> - Action 'Action_None' range [2-57] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-101] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-296] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-70] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-101] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-126] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-96] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-123] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-94] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-255] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [258-336] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [338-351] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-74] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-96] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-305] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-354] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-109] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-112] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-173] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [175-181] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-337] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [48-100] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-50] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-135] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [48-306] for track '10' has 4 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [313-317] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-160] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [162-345] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [349-351] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [3-62] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [2-107] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [128-129] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [3-20] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [24-38] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [40-41] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [60-67] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [3-52] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [2-37] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-89] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-176] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-185] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-207] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [210-341] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [345-351] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [3-102] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [103-185] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-206] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [210-260] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-49] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [53-129] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [3-25] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [27-77] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [2-27] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-32] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-55] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-68] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-140] for track '20' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [145-359] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-19] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-56] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-40] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [56-60] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-359] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-139] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [142-331] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-102] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-121] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [68-73] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-160] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [168-311] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-69] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-116] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-305] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-315] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-97] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [100-107] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-123] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [125-225] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-251] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-259] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-299] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-311] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-245] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [250-257] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-359] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [149-150] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-327] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [329-359] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-155] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-171] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [174-359] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-158] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-217] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-173] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-191] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [197-200] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [260-261] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-265] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-272] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-278] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-320] for track '40' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [323-324] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-332] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-284] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-290] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-300] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-291] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-299] for track '44' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [328-329] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [332-355] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-359] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-341] for track '50' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [350-356] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [358-359] for track '52' has 1 frames without a visible bounding box.
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
> - Player track '45' has undefined position. Will map to Position_Unknown.
> - Player track '45' has undefined team_side. Will map to Team_Unknown.
> - Player track '46' has undefined position. Will map to Position_Unknown.
> - Player track '46' has undefined team_side. Will map to Team_Unknown.
> - Player track '47' has undefined position. Will map to Position_Unknown.
> - Player track '47' has undefined team_side. Will map to Team_Unknown.
> - Player track '48' has undefined position. Will map to Position_Unknown.
> - Player track '48' has undefined team_side. Will map to Team_Unknown.
> - Player track '49' has undefined position. Will map to Position_Unknown.
> - Player track '49' has undefined team_side. Will map to Team_Unknown.
> - Player track '50' has undefined position. Will map to Position_Unknown.
> - Player track '50' has undefined team_side. Will map to Team_Unknown.
> - Player track '51' has undefined position. Will map to Position_Unknown.
> - Player track '51' has undefined team_side. Will map to Team_Unknown.
> - Player track '52' has undefined position. Will map to Position_Unknown.
> - Player track '52' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.