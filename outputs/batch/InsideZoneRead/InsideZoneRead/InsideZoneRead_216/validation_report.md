# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_216`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_216/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 40 |
| Player Tracks | 40 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 109 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [46–61], lower_priority='Action_ZoneBlock' annotated_start=49, effective_Action_ZoneBlock_start=62.
> - Action 'Action_None' range [46-242] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-294] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [46-228] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-317] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-308] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [316-329] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [46-215] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-228] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-329] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-103] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-175] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-246] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-181] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-196] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-329] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-230] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-91] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-114] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [125-129] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [131-329] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [70-80] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [101-179] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [181-237] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [239-303] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [46-189] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-216] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-329] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [46-96] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-101] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-113] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-120] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-263] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [46-59] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [62-64] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [68-76] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [49-120] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [121-317] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [49-72] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [79-96] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-83] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-95] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-106] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-188] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-303] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-311] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-329] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [112-116] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-125] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-235] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-164] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-169] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-238] for track '28' has 8 frames without a visible bounding box.
> - Action 'Action_None' range [172-174] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-223] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-273] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-282] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-317] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [227-229] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-233] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-239] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [256-257] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-252] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-257] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-263] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [270-275] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [290-291] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-274] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-289] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-325] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-327] for track '38' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.