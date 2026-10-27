# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_119`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_119/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 49 |
| Player Tracks | 49 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 171 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [48–63], lower_priority='Action_DownBlock' annotated_start=51, effective_Action_DownBlock_start=64.
> - Action 'Action_None' range [48-169] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [177-178] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-190] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-269] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-107] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-92] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-96] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-122] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [51-108] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-152] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-69] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-123] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-126] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-138] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-141] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-171] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-204] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-226] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [232-236] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [238-246] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [261-264] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-183] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-259] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-115] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [51-78] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [80-92] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [94-108] for track '8' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [117-126] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [136-143] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [145-150] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [154-156] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-266] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [48-88] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-96] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-99] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-108] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-123] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-126] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-157] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-167] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-193] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [48-78] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-86] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [88-92] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-93] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-143] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-75] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-90] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [48-122] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [88-108] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-113] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [48-92] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-96] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-102] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-108] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-115] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-119] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-143] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-170] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [175-178] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-187] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-256] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-262] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [51-102] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [107-108] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [51-97] for track '20' has 5 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [100-108] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [117-120] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-73] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-119] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-126] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-24] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-34] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-38] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-41] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-75] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-138] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-81] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-96] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-119] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-104] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-108] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-120] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-121] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-179] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-206] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-269] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-120] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-132] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-203] for track '29' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [136-143] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [151-152] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-157] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-246] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-253] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-163] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [146-269] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-158] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [162-164] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-195] for track '35' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [179-181] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-183] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-182] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-187] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-221] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-238] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [242-255] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-258] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-207] for track '39' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [209-214] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-222] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [226-232] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [199-202] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-209] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-216] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-216] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-230] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-237] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-243] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-252] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-255] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-269] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-246] for track '45' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [244-249] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-264] for track '46' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [263-264] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-269] for track '48' has 1 frames without a visible bounding box.
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