# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_318`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_318/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 41 |
| Player Tracks | 41 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 132 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Validation warning: Action 'Action_PullBlock' for track '2' (RG) duration 101 frames exceeds threshold 90 frames [start=16, end=116].
> - Validation warning: Action 'Action_DownBlock' for track '4' (LT) duration 101 frames exceeds threshold 90 frames [start=16, end=116].
> - Validation warning: Action 'Action_DownBlock' for track '13' (LG) duration 101 frames exceeds threshold 90 frames [start=16, end=116].
> - Action 'Action_None' range [13-59] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-104] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-115] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [119-160] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-175] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [16-31] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [71-80] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [82-85] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [96-98] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [100-101] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [103-111] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [124-125] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-47] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [16-36] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [48-91] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [94-113] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [180-182] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-50] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [16-59] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [13-56] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-110] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-212] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-221] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [225-226] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-59] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [65-73] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [79-80] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-15] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-84] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-139] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-104] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-246] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [252-297] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-33] for track '12' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [35-44] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-68] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-96] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-115] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [117-157] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [16-32] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [36-48] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [55-60] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [62-64] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [82-112] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' for track '13' starts at frame 117, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [117-117] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-144] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-167] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-20] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [13-15] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-86] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-115] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [117-135] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [21-27] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [31-44] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [48-58] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [79-103] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-31] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-36] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-38] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-79] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-121] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-47] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-50] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-56] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-66] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-52] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [66-113] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-131] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-157] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-63] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-71] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-91] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [93-128] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-56] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-133] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-149] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-68] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [71-75] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-73] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-89] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-96] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-101] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-133] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-79] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-86] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-97] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-158] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [176-180] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-115] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-115] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-144] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-180] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-253] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-277] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [279-280] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-258] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-128] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-149] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [154-160] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-149] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-171] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-193] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-204] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-262] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-228] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-282] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-288] for track '39' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.