# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_236`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_236/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 63 |
| Player Tracks | 63 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 139 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Segment 'Action_BallCarry' for track '3' has invalid range: start=158, end=150. Clamping end to start.
> - Validation warning: Action 'Action_PullBlock' for track '7' (RG) duration 125 frames exceeds threshold 90 frames [start=107, end=231].
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [106–121], lower_priority='Action_DownBlock' annotated_start=107, effective_Action_DownBlock_start=122.
> - Validation warning: Action 'Action_DownBlock' for track '15' (LT) duration 125 frames exceeds threshold 90 frames [start=107, end=231].
> - Action 'Action_None' range [106-134] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-241] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-246] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [135-152] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PlaySideFakeStep' range [111-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-266] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-178] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-267] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [106-308] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [107-162] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [180-182] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-258] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-224] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-270] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [107-117] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-204] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [107-126] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [130-132] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [134-138] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [195-196] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [122-140] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-259] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [261-263] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-136] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-154] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-199] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-222] for track '14' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-69] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [107-143] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [149-231] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-236] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-269] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-5] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-8] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-19] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-90] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-95] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-99] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-146] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-208] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-260] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-101] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-104] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-109] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-252] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [254-259] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-218] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [221-222] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-186] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [189-191] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-136] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-167] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-203] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-247] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [143-186] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [228-229] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-190] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [195-204] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-277] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-204] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [211-223] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [168-170] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-195] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-182] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-199] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-214] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-229] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-222] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-248] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [250-258] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-262] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-337] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-270] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-357] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-344] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-261] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-300] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-299] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-325] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-352] for track '39' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [318-324] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [328-329] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [334-336] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-324] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-348] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-324] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-323] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-330] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-342] for track '43' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [323-325] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-331] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-330] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-331] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-336] for track '48' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [332-359] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [334-342] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-359] for track '50' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [335-359] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-354] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-341] for track '53' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [337-340] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [341-342] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [344-353] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [344-354] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [348-351] for track '59' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.