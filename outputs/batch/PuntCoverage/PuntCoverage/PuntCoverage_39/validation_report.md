# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntCoverage_39`
- **Input XML**: `outputs/batch/PuntCoverage/PuntCoverage/PuntCoverage_39/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntCoverage.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 39 |
| Player Tracks | 39 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 155 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 79: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Segment 'Action_PuntBall' for track '18' has invalid range: start=84, end=67. Clamping end to start.
> - Action 'Action_None' range [26-128] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-160] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [164-166] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-174] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [26-160] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [162-179] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [181-299] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [26-110] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-117] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-137] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [26-74] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-121] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-208] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [26-202] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-132] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-157] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [26-104] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-108] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-169] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-175] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-201] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [204-206] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-164] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-299] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [26-62] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [74-127] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [26-47] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [53-55] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-162] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-86] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-158] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-176] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [181-184] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-299] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [26-71] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [74-80] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [26-50] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-59] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-159] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-178] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [182-184] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-191] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-207] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [215-222] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [224-299] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [26-70] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-91] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [94-101] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-149] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-186] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-216] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-235] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-43] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '18' starts at frame 53, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [53-53] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-57] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-61] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-67] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-72] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-84] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-151] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [153-161] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-174] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [181-184] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-191] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-205] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-221] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-37] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-299] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-94] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [96-103] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [106-111] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-119] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [129-130] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-148] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-218] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-299] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-109] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-171] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-176] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-128] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-136] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-143] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-182] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [184-185] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-188] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-191] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-217] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-233] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-221] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [145-148] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-157] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [164-166] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-161] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-204] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [231-276] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [289-291] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [293-294] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-172] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-172] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-225] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [172-191] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [220-221] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-228] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-233] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-184] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_Tackle' range [251-266] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_Tackle' range [279-299] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-213] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [216-272] for track '35' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [223-236] for track '36' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.