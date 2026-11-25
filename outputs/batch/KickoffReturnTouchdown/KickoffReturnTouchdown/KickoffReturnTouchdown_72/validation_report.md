# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `KickoffReturnTouchdown_72`
- **Input XML**: `outputs/batch/KickoffReturnTouchdown/KickoffReturnTouchdown/KickoffReturnTouchdown_72/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/KickoffReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 41 |
| Player Tracks | 41 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 130 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 509 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Row 74, Column 'Cross Goal Line': Unknown actor track ID '?' in entry '526,530,?'.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 509 as fallback play end.
> - Action 'Action_BallCarry' range [175-316] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [322-328] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [330-334] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [336-337] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [354-396] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-303] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [314-327] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-73] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-246] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-458] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-225] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [6-190] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-298] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-509] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-506] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [6-153] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-509] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-194] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-243] for track '8' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [246-247] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-148] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [151-333] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-337] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [339-347] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [355-363] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_KickApproach' range [6-32] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-332] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-140] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-249] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-309] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [322-390] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [399-489] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [491-497] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-415] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [6-64] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [71-75] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [77-159] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-259] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-330] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-339] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [341-343] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-349] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [355-382] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [384-388] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-128] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-149] for track '14' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [153-154] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-242] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-249] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-285] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-399] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-282] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-289] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-145] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-240] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-275] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-181] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [183-240] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-419] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [421-478] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-240] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [6-311] for track '21' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [316-318] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-342] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [344-345] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-362] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [373-375] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [382-490] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-66] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-116] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-158] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-196] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [173-184] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-198] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-306] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-318] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [260-394] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [266-269] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-291] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-509] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [266-271] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-304] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-449] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-303] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [343-345] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-348] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [348-465] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [377-443] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [389-391] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [393-424] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [454-462] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [431-455] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [468-469] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [475-477] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [477-509] for track '40' has 1 frames without a visible bounding box.
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
> - Metadata: no Dataset Summary row found for output_file 'KickoffReturnTouchdown_72'; source metadata written as null.

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.