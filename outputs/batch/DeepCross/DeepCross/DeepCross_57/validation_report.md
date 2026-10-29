# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `DeepCross_57`
- **Input XML**: `outputs/batch/DeepCross/DeepCross/DeepCross_57/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/DeepCross.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 65 |
| Player Tracks | 65 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 162 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [12–27], lower_priority='Action_PassBlock' annotated_start=15, effective_Action_PassBlock_start=28.
> - Action 'Action_RunDeepCrossRoute' range [27-182] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [213-215] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-221] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-221] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-235] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-243] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-247] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-178] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-160] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-166] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-209] for track '4' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [212-232] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-239] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-244] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-248] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-41] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-159] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [164-179] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-260] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-255] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-126] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-130] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-179] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-241] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-174] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [196-199] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-263] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-179] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [15-83] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-72] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-106] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-170] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [184-187] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-242] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [12-206] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-244] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [12-247] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-250] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [15-177] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [199-202] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [15-176] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [178-189] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [192-203] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [210-211] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [214-215] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [220-221] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [224-238] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [12-88] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [12-26] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [45-135] for track '19' has 5 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [137-162] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [208-216] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [220-222] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [224-243] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [15-164] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [166-178] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [188-189] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-135] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-216] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [218-240] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-245] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-249] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-53] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-59] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-135] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-235] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [94-173] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-206] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-246] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-110] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-135] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-163] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-179] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [244-245] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-173] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-189] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-199] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-206] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [208-215] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [220-233] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-248] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-189] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-197] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [200-202] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-235] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-244] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-239] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-246] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-214] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-243] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-231] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-246] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-250] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-232] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-245] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [228-235] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [238-241] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-247] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-251] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-318] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-268] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-287] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-300] for track '39' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [309-311] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-319] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-319] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [284-288] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-318] for track '42' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [284-318] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [356-366] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-286] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-318] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-319] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-318] for track '46' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [291-300] for track '47' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [302-305] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-314] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-319] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [359-389] for track '63' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [378-379] for track '64' has 1 frames without a visible bounding box.
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
> - Player track '60' has undefined position. Will map to Position_Unknown.
> - Player track '60' has undefined team_side. Will map to Team_Unknown.
> - Player track '61' has undefined position. Will map to Position_Unknown.
> - Player track '61' has undefined team_side. Will map to Team_Unknown.
> - Player track '62' has undefined position. Will map to Position_Unknown.
> - Player track '62' has undefined team_side. Will map to Team_Unknown.
> - Player track '63' has undefined position. Will map to Position_Unknown.
> - Player track '63' has undefined team_side. Will map to Team_Unknown.
> - Player track '64' has undefined position. Will map to Position_Unknown.
> - Player track '64' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.