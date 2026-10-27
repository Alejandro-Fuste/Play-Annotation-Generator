# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_155`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_155/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 100 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 312: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [31-238] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-208] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-222] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-147] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [154-214] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [217-218] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-73] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-93] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-113] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-116] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-131] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-198] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [31-239] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-137] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-143] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-228] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [73-112] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [117-228] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [230-231] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-54] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-175] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [178-182] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-83] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-113] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-116] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-112] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [105-117] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-124] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [37-44] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [47-60] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [73-237] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-145] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [167-168] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-95] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-113] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-132] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-239] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-60] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [37-85] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [65-116] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [71-117] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-239] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-124] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-144] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-147] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-131] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-225] for track '25' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [115-116] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-239] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-160] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [165-168] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-174] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [177-195] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-225] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-159] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [155-161] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-205] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [196-199] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-205] for track '34' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.