# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_148`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_148/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 37 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 134 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_DownBlock' range [116-152] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [116-136] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [140-157] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-249] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-228] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [231-232] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-235] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-249] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-258] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-298] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-79] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-90] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-93] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-97] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-106] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [116-146] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [149-155] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [157-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [182-185] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-167] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-299] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-56] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-75] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-123] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-141] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [153-164] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [155-200] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [202-264] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [266-270] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-149] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-37] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-51] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-83] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-111] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-116] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-141] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [159-232] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [245-266] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [116-170] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-202] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-234] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-118] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-219] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [221-227] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-235] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [241-272] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-290] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-143] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-207] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-8] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-18] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-75] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-106] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-118] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-160] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-175] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-128] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [122-125] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-272] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-280] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-141] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-149] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-187] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [198-201] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-205] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-213] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-226] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [229-265] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [285-286] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-147] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-155] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-173] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-213] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [162-272] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-299] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-187] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [170-176] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-180] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [183-200] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [221-234] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [242-243] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-211] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-224] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [231-232] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-263] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [272-299] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [228-242] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-247] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-235] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [244-249] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-270] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [275-277] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-282] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-249] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-266] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-249] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-258] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [268-269] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-266] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-269] for track '35' has 1 frames without a visible bounding box.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.