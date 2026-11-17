# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_226`
- **Input XML**: `outputs/batch/Power/Power/Power_226/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 105 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Action 'Action_PreSnap' range [8-62] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-73] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-125] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-275] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-33] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-313] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [316-360] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-89] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-93] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-144] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-294] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [296-297] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-78] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-42] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-259] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-273] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [276-298] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-85] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-151] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-167] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-50] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-55] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-24] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-36] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-202] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [264-290] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [293-309] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [310-361] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-50] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-181] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-192] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-205] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-233] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-239] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-340] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-26] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-381] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-40] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-153] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-343] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-12] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-22] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-217] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-338] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [350-358] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-10] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-42] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-48] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-51] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-72] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-42] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-60] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-178] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [264-275] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-169] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-189] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [264-303] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-356] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-370] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [374-419] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-263] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-315] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [340-387] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [392-393] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [266-276] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [267-285] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [290-354] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [366-372] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [278-289] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [310-313] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-316] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [328-332] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [290-291] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [299-317] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [319-323] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [329-330] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [308-317] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [330-351] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [360-373] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [310-316] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [346-350] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [358-399] for track '26' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [401-419] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [313-333] for track '27' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [331-366] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [370-371] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [378-379] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [382-387] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [334-384] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [361-389] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [375-399] for track '31' has 1 frames without a visible bounding box.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.