# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntCoverage_88`
- **Input XML**: `outputs/batch/PuntCoverage/PuntCoverage/PuntCoverage_88/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntCoverage.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 60 |
| Player Tracks | 60 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 154 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 177: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - Row 178: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Action 'Action_PreSnap' range [0-99] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-110] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-326] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [329-334] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [339-341] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-115] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [95-163] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-125] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-139] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-152] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-60] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-158] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-126] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-40] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-177] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-188] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-201] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-184] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-158] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-182] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-186] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-57] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-182] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-186] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-176] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-188] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-194] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-205] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-117] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-146] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-81] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-98] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-86] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-121] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-150] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-133] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-147] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-151] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-53] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-309] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_Tackle' range [310-318] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_Tackle' range [320-323] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-339] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [343-346] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [351-352] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-45] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-65] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-40] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-95] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-101] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-117] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-137] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-168] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-270] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-22] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-77] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-47] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-93] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-109] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-173] for track '23' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-188] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-194] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-201] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-207] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-219] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-98] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-122] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-125] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-113] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-125] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-162] for track '26' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-175] for track '27' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-183] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-132] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-140] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-169] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-182] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-138] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [234-314] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-325] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [328-353] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-174] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-155] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-359] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-153] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-165] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-168] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-180] for track '35' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-184] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-188] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-218] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-232] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [246-248] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-171] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-158] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-168] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-199] for track '37' has 8 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-206] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-215] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [296-298] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [304-305] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [309-310] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-173] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-173] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-207] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-187] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-359] for track '42' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-203] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-229] for track '44' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-257] for track '44' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-296] for track '45' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [298-305] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [310-325] for track '45' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [327-339] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [341-347] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-287] for track '47' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [289-298] for track '47' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [301-305] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [314-348] for track '47' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [351-352] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [276-282] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-298] for track '48' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [300-310] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [321-324] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [326-348] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [351-352] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [355-359] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [291-292] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [296-298] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [314-315] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [352-353] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [297-299] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [307-312] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [319-324] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [330-348] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [337-351] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [340-352] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [342-351] for track '59' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '53' has undefined position. Will map to Position_Unknown.
> - Player track '53' has undefined team_side. Will map to Team_Unknown.
> - Player track '54' has undefined position. Will map to Position_Unknown.
> - Player track '54' has undefined team_side. Will map to Team_Unknown.
> - Player track '55' has undefined position. Will map to Position_Unknown.
> - Player track '55' has undefined team_side. Will map to Team_Unknown.
> - Player track '56' has undefined position. Will map to Position_Unknown.
> - Player track '56' has undefined team_side. Will map to Team_Unknown.
> - Player track '57' has undefined position. Will map to Position_Unknown.
> - Player track '57' has undefined team_side. Will map to Team_Unknown.
> - Player track '58' has undefined position. Will map to Position_Unknown.
> - Player track '58' has undefined team_side. Will map to Team_Unknown.
> - Player track '59' has undefined position. Will map to Position_Unknown.
> - Player track '59' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.