# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntCoverage_52`
- **Input XML**: `outputs/batch/PuntCoverage/PuntCoverage/PuntCoverage_52/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntCoverage.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 49 |
| Player Tracks | 49 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 119 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Segment 'Action_Tackle' for track '4' has invalid range: start=249, end=227. Clamping end to start.
> - Action 'Action_PreSnap' range [0-100] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-108] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-130] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-135] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-141] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-148] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-162] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-14] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-41] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-247] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-69] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-156] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-171] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-227] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-46] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-60] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-163] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-261] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-134] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-19] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-14] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-20] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-29] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-60] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-25] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-32] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-166] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-42] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-110] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-176] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-114] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-117] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-44] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-16] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-27] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-162] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-23] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-29] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-152] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-14] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-95] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-23] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-49] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-162] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-168] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-236] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-247] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-260] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-269] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-25] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-32] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-62] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-66] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-7] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-23] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-29] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-115] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-42] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-45] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-63] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-66] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-72] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-78] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-148] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-152] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-161] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-175] for track '23' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-269] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-42] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-178] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-177] for track '27' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-192] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-78] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-147] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-151] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-227] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-58] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-69] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-175] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-204] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-227] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-171] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-95] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-101] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [164-194] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [208-226] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-160] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-161] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-183] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-215] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-225] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-218] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-226] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-227] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-243] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-248] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-253] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-226] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-267] for track '45' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-249] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-263] for track '47' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.