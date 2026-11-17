# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_5`
- **Input XML**: `outputs/batch/Power/Power/Power_5/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 77 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Action 'Action_PreSnap' range [16-336] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [339-348] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [350-354] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [356-365] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-325] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [328-331] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [335-340] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [342-344] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [357-368] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [372-389] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-381] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [385-389] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-304] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [310-389] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-350] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [352-353] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [359-389] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-367] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [370-383] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-335] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [348-356] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [369-376] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [379-389] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-278] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [280-305] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-229] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-389] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-236] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-272] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [291-296] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [298-301] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [305-389] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-288] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-345] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [347-348] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [363-389] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-244] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-261] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [269-341] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-241] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-248] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-272] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [277-279] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [282-300] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [302-310] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-296] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [298-370] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [372-376] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [220-227] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [232-233] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [238-269] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [220-283] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-225] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-230] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-277] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-350] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [356-368] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [375-377] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [379-380] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [271-272] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [316-334] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [343-389] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-298] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [317-319] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [321-389] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [369-389] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [386-389] for track '28' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.