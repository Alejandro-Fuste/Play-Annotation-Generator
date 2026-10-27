# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_273`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_273/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 38 |
| Player Tracks | 38 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 115 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [81–93], lower_priority='Action_DownBlock' annotated_start=84, effective_Action_DownBlock_start=94.
> - Action 'Action_None' range [81-379] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [84-138] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [140-142] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [145-146] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-149] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-272] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-279] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [281-286] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-134] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-156] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [81-330] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [333-340] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [343-346] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-127] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-239] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-248] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-281] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [94-102] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [127-129] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-240] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-309] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-152] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-163] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [81-167] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-389] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [81-144] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-156] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [84-86] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [88-106] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [134-139] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [141-145] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-172] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [175-178] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-389] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-136] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-389] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-83] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [84-85] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [88-100] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-188] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-240] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-11] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-111] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-240] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-11] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-93] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [121-122] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-162] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-232] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [81-125] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-20] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-165] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [170-178] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [180-196] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-227] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-234] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-183] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [175-389] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [176-178] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-213] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [224-226] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-246] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [250-378] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [382-389] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-304] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-389] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [321-337] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-332] for track '35' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.